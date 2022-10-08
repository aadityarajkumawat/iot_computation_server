def pulse_data_validator(data: dict):
    required_keys = ["abpm", "bpm", "ir", "timestamp"]

    has_data = False
    for k in data.keys():
        if k == 'data':
            has_data = True

    if not has_data:
        return False

    data: list = data['data']

    first: dict = data[0]

    has_all_keys = True
    for k in first.keys():
        print(k, required_keys.count(k))
        if required_keys.count(k) != 1:
            has_all_keys = False

    if not has_all_keys:
        return False

    return True 