import cv2

path = r'C:\Users\luciv\AppData\Local\Programs\Python\Python311\testeJornal.jpeg'

imagem = cv2.imread(path)

detector_face = cv2.CascadeClassifier(r'C:\Users\luciv\AppData\Local\Programs\Python\Python311\haarcascade_frontalface_default.xml')

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)  

#cv2.imshow('imagem cinza', imagem_cinza)

deteccoes = detector_face.detectMultiScale(imagem_cinza, scaleFactor=1.1, minSize=(2, 2))

for (x, y, l, a) in deteccoes:
  #print(x, y, l, a)
  cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)

cv2.imshow('Deteccao facial', imagem)

cv2.waitKey(0)

cv2.destroyAllWindows()