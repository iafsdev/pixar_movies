from joblib import load 
import warnings

warnings.filterwarnings('ignore')

name = input('Ingresa el nombre de la pelicula: ')
year = input('¿En qué año se estrenó? ')
score = input('¿Qué puntuación obtuvo en IMDB? ')
opening = input('¿Cúanto obtuvo en su primer fin de semana? (ej. 100 = $100,000,000): ')

values = [year, 0, 0, score, 0, opening, 0, 0, 0]

model = load('./models/worldwide_gross.joblib')
pred = model.predict([values])
print(f'Se estima que {name} obtenga una taquilla de: ${pred[0]:.8f} MDD')
