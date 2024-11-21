import dask.dataframe as dd
import warnings



# Подавление всех предупреждений
warnings.filterwarnings("ignore")


def dask_advanced_analysis(ddf):
    # Фильтрация данных
    filtered_ddf = ddf[ddf['Year'] > 2005].compute()
    print("\nФильтрация (Year > 2005):")
    print(filtered_ddf.head())

    # Группировка по странам
    grouped = ddf.groupby('Country')['общий показатель экономической производительности, учитывающий рост и инфляцию'].mean().compute()
    print("\nСредний показатель производительности по странам:")
    print(grouped)

    # Корреляция между экономическим ростом и инфляцией
    correlation = ddf[['Экономический рост', 'Инфляция']].corr().compute()
    print("\nКорреляция между экономическим ростом и инфляцией:")
    print(correlation)

    # Сортировка
    sorted_ddf = ddf.sort_values(by='Year', ascending=False).head(5)
    print("\nСортировка по годам (по убыванию):")
    print(sorted_ddf)

    return filtered_ddf, grouped, correlation

def dask_basic_analysis(file_path):
    """
    Загружает данные с помощью Dask и выводит базовую информацию.
    """
    try:
        # Загрузка данных
        ddf = dd.read_csv(file_path)
        print("\nДанные успешно загружены с помощью Dask:")
        print(ddf.head())  # Показать первые 5 строк

        # Описательная статистика
        print("\nОписательная статистика (Dask):")
        print(ddf.describe().compute())

        return ddf
    except Exception as e:
        print(f"Ошибка при обработке данных с помощью Dask: {e}")
        return None