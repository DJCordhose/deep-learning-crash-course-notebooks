sample_df = df.sample(n=300, random_state=42)
sns.set(font_scale=2)
sns.pairplot(sample_df, hue="group", palette={0: '#AA4444', 1: '#006000', 2: '#EEEE44'}, 
             vars=['speed', 'age', 'miles'], height=5, markers=["o", "s", "D"])