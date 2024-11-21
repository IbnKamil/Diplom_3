from pandas_analysis import pandas_basic_analysis, pandas_advanced_analysis
from dask_analysis import dask_basic_analysis, dask_advanced_analysis
from visualizations import create_visualizations
import warnings
import time


# Подавление всех предупреждений
warnings.filterwarnings("ignore")


def main():
    # Путь к файлу
    file_path = r"C:\Users\Magom\PYTHON\python_Diplom\sample_dataset.csv"

    # Анализ с использованием Pandas
    print("Обработка данных с Pandas:")
    start_time_pandas = time.time()  # Старт измерения времени
    pandas_df = pandas_basic_analysis(file_path)
    if pandas_df is not None:
        pandas_advanced_analysis(pandas_df)
    end_time_pandas = time.time()  # Конец измерения времени
    pandas_time = end_time_pandas - start_time_pandas
    print(f"Время обработки данных с Pandas: {pandas_time:.2f} секунд")

    # Анализ с использованием Dask
    print("\nОбработка данных с Dask:")
    start_time_dask = time.time()  # Старт измерения времени
    dask_ddf = dask_basic_analysis(file_path)
    if dask_ddf is not None:
        dask_advanced_analysis(dask_ddf)
    end_time_dask = time.time()  # Конец измерения времени
    dask_time = end_time_dask - start_time_dask
    print(f"Время обработки данных с Dask: {dask_time:.2f} секунд")

    # Создание визуализаций
    print("\nСоздание визуализаций:")
    if pandas_df is not None:  # Передаем DataFrame
        create_visualizations(pandas_df)

    # Сравнение времени выполнения
    print("\nСравнение времени выполнения:")
    print(f"Pandas: {pandas_time:.2f} секунд")
    print(f"Dask: {dask_time:.2f} секунд")
    if pandas_time < dask_time:
        print("Pandas оказался быстрее.")
    else:
        print("Dask оказался быстрее.")


if __name__ == "__main__":
    main()
