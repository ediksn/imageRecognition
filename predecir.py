import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

altura, longitud = 100,100
modelo = './modelo/modelo.h5'
pesos = './modelo/pesos.h5'
cnn = load_model(modelo)
cnn.load_weights(pesos)

def predecir(file):
    var = load_img(file, target_size=(longitud, altura))
    var = img_to_array(var)
    var = np.expand_dims(x, axis=0)
    arr = cnn.predecir(var)
    resul = arr[0]
    respuesta = np.argmax(resul)
    if respuesta==1:
        print('La imagen corresponde a un girasol')
    elif respuesta==2
        print('La imagen corresponde a una rosa')
    elif respuesta==3:
        print('La imagen corresponde a un tulipan')

predecir('prueba.jpg')