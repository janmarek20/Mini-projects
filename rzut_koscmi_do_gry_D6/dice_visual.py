from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Rzut dwiema koścmi D6.

#Utworzenie kości typu D6.
die_1 = Die()
die_2 = Die()

#Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = []
for roll_num in range(1000):
    result = die_1.roll() +die_2.roll()
    results.append(result)

#Analiza wyników.
frequencies = []
max_result = die_1.num_sides +die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#Wizualizacja wyników.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Wynik', 'dtick': 1}
y_axis_config = {'title': 'Częstotoliwość występowania wartości'}
my_layout = Layout(title='Wynik rzucania dwiema kośćmi D6 tysiąc razy',
                   xaxis = x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')