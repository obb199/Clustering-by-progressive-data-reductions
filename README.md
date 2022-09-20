# Clustering by progressive data reduction
1 - calculate the distance from each point to the other N-1 points.
2 - swap the nearest pairs of points for a new point that is the average of the double.
3 - repeat steps 1 and 2 until the set has a predetermined amount of k points or the number of points is less than k.
4 - if the new amount of points is less than the given, it will be necessary to regress the set to the previous iteration and join the two points closer to reaching k. 
5 - the remaining k points will be used as a reference for groupings. 
6 - for a new point p outside the set, p has k distances and will belong to the group where the distance is shorter.

# Clusterização por redução progressiva de dados
1 - calcular a distância de cada ponto até os n-1 outros pontos.
2 - trocar os pares de pontos mais próximos por um novo ponto que seja a média da dupla.
3 - repetir os passos 1 e 2 até que o conjunto possua uma quantidade pré-determinada de k pontos ou que o número de pontos seja menor que k.
4 - caso a nova quantidade de pontos seja menor que o determinado, será necessário regredir o conjunto à iteração anterior e juntar os dois pontos mais próximos até atingir k.
5 - os k pontos que sobrarem serão utilizados como referência para agrupamentos.
6 - para um novo ponto p fora do conjunto, p possui k distâncias e pertencerá ao grupo em que a distância for menor.

# Examples of results // Exemplos de resultados:
![test for readme](https://user-images.githubusercontent.com/74666057/190880229-eb2cf336-a485-4811-93f7-ce74797c94d9.png)

![curves for readme](https://user-images.githubusercontent.com/74666057/190880275-221bfaf8-9e0f-4d2d-9b73-9ea125d4013b.png)

**you can find the code of these examples and others in the project ("tests" file).
