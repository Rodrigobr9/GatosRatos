#
# Dada uma matriz quadrada e um certo numero de gatos e ratos, encontrar as solucoes para dispor todos os animais na matriz
# de maneira que so animais da mesma especie podem estar numa mesma linha, coluna e diagonal
#
# A primeira parte da solução varre uma matriz colocando os gatos em todas as combinações possíveis. A cada nova combinacao
# chama-se a função que verifica se, eliminadas as linhas, colunas e diagonais ocupadas pelos gatos, restam possicoes livres
# suficientes para alocar todos os ratos.
#
# Rodrigo Pires - 17 dezembro 2019 
# pires.rodrigo@gmail.com
# 
print('Tamanho da matriz : ')
tam = int(input())
print('Quantos Gatos : ')
ng = int(input())
print('Quantos Ratos : ')
nr = int(input())
#
## Inicializa array
pos=[]
matriz = tam * tam
totalSolucoes=0

if matriz <= ng:
	print ('Nao ha solucoes possiveis')
# endif

i=0
ngx=1
while i < ng:
	pos.append(ngx)
	i+=1
	ngx+=1
#print('Posicoes : ', pos[:])
#
level = ng-2 
possivel = True
iter=1		

while possivel:

	i = pos[ng-1]

	arr_matriz=[]
	ind=1
	while ind <= matriz:
		arr_matriz.append("")
		ind +=1
	#endwhile
	
	while i <= matriz: #Loop que varia a ultima posicao do array
#		verifica_ratos(pos) # chama funcao que verifica se existem celulas livres

		# print('--------------------')
		# print('Iteracao : % 2d ' %(iter))
		# print('Posicoes Gatos  : ', pos[:])

		livres=matriz
		# print ('Livres Inicial : ', livres)
		arr_matriz.clear()
		ind=1

		while ind <= matriz:
			arr_matriz.append("")
			ind +=1
		#endwhile

		ix=0

		while ix <= ng - 1 and livres >= nr:
		
			# print ('Elemento : ', ix+1, ' de: ', ng)
			# Linha e Coluna
			lin=int((pos[ix]-1)/tam)
			col=(pos[ix]-1)-tam*lin
			# print ('Linha : ', lin, ' Coluna: ', col)
			aux=0
			while aux <= tam-1:
				aux_lin = tam * lin + aux
				if arr_matriz[aux_lin] == "":
					arr_matriz[aux_lin] = "X"
					livres -=1
					
				aux_col = tam * aux + col 
				if arr_matriz[aux_col] == "":
					arr_matriz[aux_col] = "X"
					livres -=1
		
				aux+=1
			#endwhile
			# print ('Livres Lin e Col: ', livres)

			## Diagonais
			#NE
			
			nel=lin-1
			nec=col + 1
			while nel >= 0 and nec <= tam - 1:
				posaux = tam * nel + nec
				if arr_matriz[posaux]=="":
					arr_matriz[posaux]="X"
					livres-=1
				nel -= 1
				nec += 1
			
			#endwhile
			# print ('Livres NE : ', livres)
	
			#SE
			sel=lin+1
			sec=col + 1
			while sel <= tam-1 and sec <= tam - 1:
				posaux = tam * sel + sec
				if arr_matriz[posaux]=="":
					arr_matriz[posaux]="X"
					livres-=1
				sel += 1
				sec += 1
			
			#endwhile
			# print ('Livres SE : ', livres)

			#SW
			swl=lin+1
			swc=col - 1
			while swl <= tam-1 and swc >= 0:
				posaux = tam * swl + swc
				if arr_matriz[posaux]=="":
					arr_matriz[posaux]="X"
					livres-=1
				swl += 1
				swc -= 1
			
			#endwhile
			# print ('Livres SW : ', livres)
	
			#NW
			nwl=lin-1
			nwc=col - 1
			while nwl >= 0 and nwc >= 0:
				posaux = tam * nwl + nwc
				if arr_matriz[posaux]=="":
					arr_matriz[posaux]="X"
					livres-=1
				nwl -= 1
				nwc -= 1
			
			#endwhile
			# print ('Livres NW : ', livres)

			ix+=1
			
		#endwhile
		# print ('Livres Final: ', livres)
		if livres >= nr:
			totalSolucoes += 1
			print('--------------------')
			print('Iteracao : % 2d ' %(iter))
			print('Posicoes Gatos  : ', pos[:])
			print ('Array OK : ', arr_matriz[:])
		#endif
		iter += 1
		i += 1
		pos[ng-1]+=1
		
	# end while
	##Fim Verifica Ratos
	##		
	pos[ng-1]=pos[ng-2]+1 # reestabelece o array
	# print ('Pos Restab : ', pos[:], ' Level: ',level)
		
	if pos [level] < matriz - (ng - (level + 1)):
		j = level
		aux = (ng-1)
		while j <= aux:
			pos[j] += 1
			j += 1
		#end while
		#print ('Pos vaiando level : ', pos[:])

	else:
		level= level - 1
		loop = True
		while loop:
			
			while level >= 0:
				if pos[level] >= matriz - (ng-(level+1)):
					level = level-1
				else:
					break
				#endif
			#end while
				
			if level < 0:
				loop = False
				possivel = False
			else:
				next = pos[level] + 1
				x = level
				while x <= ng - 1:
					pos[x] = next
					next = next + 1
					x += 1
				#endwhile
				loop = False # existem alternativas possivel
			#endif
				
		#end while
				
		if possivel:
			level = ng - 2
		else:
			possivel = False #ACABOU
		#endif						
	#endif
	#print ('Pos variano LEVEL: ', pos[:])

#end while 
print ('==============================')
print ('Total Solucoes  : ', totalSolucoes)