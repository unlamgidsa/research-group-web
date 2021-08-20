def detect_anomalies_with_rolling_mean(ts, num_stds, window, var_name='Value'):
    # Gather statistics in preparation for outlier detection
    rolling_mean = ts.rolling(window=window, center=False).mean()
    first_window_mean = ts.iloc[:window].mean()
    for i in range(window):  # fill first 'window' samples with mean of those samples
        rolling_mean[i] = first_window_mean
    std = float(ts.values.std(ddof=0))
    X = ts.values
    outliers = pd.Series(dtype=np.float64)
    time_series_with_outliers = pd.DataFrame({var_name: ts})
    time_series_with_outliers['Outlier'] = 'False'

    # Label outliers using standard deviation
    for t in range(len(X)):
        obs = X[t]
        y = rolling_mean[t]
        if abs(y-obs) > std*num_stds:
            time_series_with_outliers.at[ts.index[t], 'Outlier'] = 'True'
            outlier = pd.Series(obs, index=[ts.index[t]])
            outliers = outliers.append(outlier)

    return time_series_with_outliers, outliers

