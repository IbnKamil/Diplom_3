import pandas as pd
import warnings



# Подавление всех предупреждений
warnings.filterwarnings("ignore")


def pandas_advanced_analysis(df):

    # Фильтрация данных
    filtered_df = df[df['Year'] > 2005]
    print("\nФильтрация (Year > 2005):")
    print(filtered_df.head())

    # Группировка по странам
    grouped = df.groupby('Country')['общий показатель экономической производительности, учитывающий рост и инфляцию'].mean()
    print("\nСредний показатель производительности по странам:")
    print(grouped)

    # Корреляция между экономическим ростом и инфляцией
    correlation = df[['Экономический рост', 'Инфляция']].corr()
    print("\nКорреляция между экономическим ростом и инфляцией:")
    print(correlation)

    # Сортировка
    sorted_df = df.sort_values(by='Year', ascending=False)
    print("\nСортировка по годам (по убыванию):")
    print(sorted_df.head())

    return filtered_df, grouped, correlation

def pandas_basic_analysis(file_path):
    """
    Загружает данные с помощью Pandas и выводит базовую информацию.
    """
    try:
        # Загрузка данных
        df = pd.read_csv(file_path)
        print("\nДанные успешно загружены с помощью Pandas:")
        print(df.head())  # Показать первые 5 строк

        # Описательная статистика
        print("\nОписательная статистика (Pandas):")
        print(df.describe(include='all'))

        return df
    except Exception as e:
        print(f"Ошибка при обработке данных с помощью Pandas: {e}")
        return None