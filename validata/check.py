import numpy as np
import errors

# TODO: Cache the covariance matrix
# TODO: Optionally warn, instead of error
# TODO: Check non-stationarity
# TODO: Dynamic threshold for condition number based on type?

def check(data=None, labels=None):
    rng = np.random.RandomState()
    init_rng_state = rng.get_state()
    np.random.seed(0)

    _data = None if data is None else np.array(data)
    _labels = None if labels is None else np.array(labels)

    if _data is not None:
        check_constant_columns(_data)
        check_ill_conditioned(_data)
    if _labels is not None:
        check_labels_are_1d_or_2d(_labels)
        if labels_are_one_hot(_labels):
            check_all_classes_used(_labels)
        elif labels_are_integer(_labels):
            check_classes_are_contiguous(_labels)
        elif labels_are_strings(_labels):
            continue
    if _labels is not None and _data is not None:
        check_statistically_significant_splits(_data,_labels)

    rng.set_state(init_rng_state)

def check_constant_columns(data):
    for i,column in enumerate(data.T):
        if np.all(column==column[0]):
            raise errors.ConstantVariableError("Column {} is constant. Is that intended?".format(i))

def check_ill_conditioned(data, bit_threshold=12):
    C = np.cov(data,rowvar=0)
    cond = np.linalg.cond(C)
    if np.log10(cond) >= bit_threshold:
        raise errors.IllConditionedError("Covariance matrix of data is ill conditioned: {:.2E}. Try whitening your data.".format(cond))

def check_labels_are_1d_or_2d(labels):
    if labels.ndim not in (1,2):
        raise errors.LabelsWrongSizeError("Label array dimension is {}. Should be 1 or 2.".format(labels.ndim))

def labels_are_one_hot(labels):
    if labels.ndim == 1:
        return False
    if np.all(np.sum(np.abs(labels),axis=1)==1):
        return True
    else:
        return False

def labels_are_strings(labels):
    return labels.dtype.kind == 'S'

def labels_are_integer(labels):
    return labels.dtype.kind == 'i'

def labels_are_float(labels):
    return labels.dtype.kind == 'f'

def check_all_classes_used(labels):
    return np.all(np.sum(labels,axis=0)>0)

def check_classes_are_contiguous(labels):
    return np.all(np.diff(np.unique(labels))==1)

def check_statistically_significant_splits(data, labels):
    pass

def check_stationarity(data_old, data_new):
    pass
