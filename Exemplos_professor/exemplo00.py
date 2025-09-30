import cv2
ddepth = cv2.CV_16S
# Carrega imagen "frame.png" em escala de cinza
gray = cv2.imread("goku.png",cv2.IMREAD_GRAYSCALE)
# calcula derivada de primeira ordem na direção x 
grad_x = cv2.Sobel(gray, ddepth, 1, 0, ksize=3,scale = 1)
# calcula derivada de primieira ordem na direção y
grad_y = cv2.Sobel(gray, ddepth, 0, 1, ksize=3,scale = 1)

# calcula valor absoluto e converte para uint8 
abs_grad_x = cv2.convertScaleAbs(grad_x)
abs_grad_y = cv2.convertScaleAbs(grad_y)

# Calcula gradiente
grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
# concatena image gerada com a original
saida=cv2.hconcat((grad,gray))
# redimenciona em 60%
saida=cv2.resize(saida,None,None,0.4,0.4)
#salva imagem
cv2.imwrite("saida.png",saida)
cv2.imshow("janela", saida)
cv2.waitKey(0)
