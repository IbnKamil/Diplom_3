import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Подавление всех предупреждений
warnings.filterwarnings("ignore")


def create_visualizations(df):

    # Убираем нечисловые столбцы
    numeric_df = df.select_dtypes(include=["number"])

    # Проверяем, есть ли числовые данные
    if numeric_df.empty:
        print("В DataFrame нет числовых данных для создания визуализаций.")
        return

    # Линейный график
    plt.figure(figsize=(10, 6))
    df.groupby('Year')['общий показатель экономической производительности, учитывающий рост и инфляцию'].mean().plot(kind='line')
    plt.title("Средний показатель производительности по годам")
    plt.xlabel("Год")
    plt.ylabel("Производительность")
    plt.show()

    # Гистограмма
    first_numeric_column = numeric_df.columns[3]
    plt.figure()
    numeric_df[first_numeric_column].hist(bins=15, edgecolor="black")
    plt.title(f"Гистограмма для {first_numeric_column}")
    plt.xlabel(first_numeric_column)
    plt.ylabel("Частота")
    print(numeric_df.columns)
    plt.show()

    # Круговая диаграмма
    plt.figure(figsize=(8, 8))
    df['Country'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title("Распределение данных по странам")
    plt.ylabel("")
    plt.show()

    # Тепловая карта
    # Убираем нечисловые столбцы
    numeric_df = df.select_dtypes(include=["number"])

    # Проверяем, есть ли числовые данные
    if numeric_df.empty:
        print("В DataFrame нет числовых данных для создания корреляционной матрицы.")
        return

    # Корреляционная матрица
    correlation_matrix = numeric_df.corr()

    # Построение тепловой карты с аннотациями
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", annot_kws={"size": 10}, linewidths=0.5)
    plt.title("Корреляционная матрица", pad=20)
    plt.show()

    # Box Plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Country', y='Экономический рост', data=df)
    plt.title("Распределение экономического роста по странам")
    plt.xlabel("Страна")
    plt.ylabel("Экономический рост")
    plt.xticks(rotation=45)
    plt.show()