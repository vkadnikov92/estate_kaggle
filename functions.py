# Функция краткой аналитики по колонке
def col_analytics(col, df):
    print(f'Число NaN: {df[col].isna().sum()}')
    print(f'Число уникальный значений: {subm_df[col].nunique()}')
    print(df[col].value_counts())
    sns.histplot(df[col])

# Функция выгрузки результатов
def res_2_csv(id_column, predictions_column, file_name='submission.csv'):
    # Создаем DataFrame из переданных столбцов
    df = pd.DataFrame({ 'Id': id_column, 'SalePrice': predictions_column })
    # Сохраняем DataFrame в CSV-файл
    df.to_csv(file_name, index=False)

# Функция локального расчета RMSE метрики
def get_score(model, X, y):
    model.fit(X, y.ravel())

    # Получаем предсказания на тестовых данных
    y_pred = model.predict(X)

    # Вычисляем среднеквадратическую ошибку (MSE)
    mse = mean_squared_error(y, y_pred)

    # Получаем корень из MSE, чтобы получить RMSE
    rmse = np.sqrt(mse)

    return f'Значение метрики RMSE: {rmse}'