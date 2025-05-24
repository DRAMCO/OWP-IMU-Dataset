import numpy as np
import os

def op_data_preprocessing(gt_data, op_data, time_interval=0.01, min_distance_interval=0.05):
    """
    Preprocess optical positioning data by synchronizing with ground truth data and filtering out
    points that are too close together.

    Parameters:
      gt_data: np.ndarray
          Ground truth data array. Assumed columns:
            - Column 0: timestamp
            - Columns 1-4: positions (x, y, z)
            - Columns 4-13: flattened 3x3 rotation matrix (row-major order)
      op_data: np.ndarray
          Optical positioning data array. Assumed columns:
            - Column 0: timestamp
            - Columns 1-5: RSS values
      time_interval: float, optional
          Maximum allowed time difference between GT and OP data.
      min_distance_interval: float, optional
          Minimum allowed Euclidean distance between consecutive accepted positions.
          
    Returns:
      result: np.ndarray
          Array with each row formatted as: [gt_timestamp, op_timestamp, x, y, z, RSS1, ..., RSS4]
    """
    result_list = []
    last_accepted_pos = None

    for op_row in op_data:
        op_ts = op_row[0]
        
        # Find the gt_data row with the closest timestamp to op_ts
        time_diffs = np.abs(gt_data[:, 0] - op_ts)
        idx = np.argmin(time_diffs)
        min_diff = time_diffs[idx]
        
        # If the time difference exceeds the threshold, skip this op_data row
        if min_diff > time_interval:
            continue

        # Get the matching gt_data row
        gt_row = gt_data[idx]
        gt_ts = gt_row[0]
        pos = gt_row[1:4]  # Extract x, y, z

        # Filter: only accept points if the distance from the last accepted position is >= min_distance_interval
        if last_accepted_pos is not None:
            distance = np.linalg.norm(pos - last_accepted_pos)
            if distance < min_distance_interval:
                continue
        
        # Update the last accepted position
        last_accepted_pos = pos.copy()
        rss_values = op_row[1:5]
        
        # Combine the result: gt_timestamp, op_timestamp, x, y, z, RSS1,...,RSS4
        combined = np.concatenate(([gt_ts, op_ts], pos, rss_values))
        result_list.append(combined)
    
    result = np.array(result_list)
    print(f"Original OP data: {op_data.shape[0]} rows, Processed OP data: {result.shape[0]} rows")
    return result




def read_GT_Rotation_matrix_list(gt_data):
    """
    Extract rotation matrices from the GT data and store them in a list.
    
    Parameters:
        gt_data: np.ndarray
            Ground truth data array. Assumes each row is formatted as:
              - Column 0: timestamp
              - Columns 1-3: position (x, y, z)
              - Columns 4-12: flattened rotation matrix (3x3 matrix in row-major order)
    
    Returns:
        GT_Rotation_matrix_list: list of np.ndarray
            A list where each element is a 3x3 rotation matrix.
    """
    GT_Rotation_matrix_list = []
    
    for row in gt_data:
        # Extract columns 4 to 13, convert to float, and reshape into a 3x3 matrix (row-major order)
        rot_mat = row[4:13].astype(float).reshape((3, 3), order='C')
        GT_Rotation_matrix_list.append(rot_mat)
    
    return GT_Rotation_matrix_list


