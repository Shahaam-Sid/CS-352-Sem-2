class VertexCheck:
    def __init__(self, list_of_vertices_shape_one: list,
                 list_of_vertices_shape_two: list):
        self.vertex_list_1 = list_of_vertices_shape_one
        self.vertex_list_2 = list_of_vertices_shape_two
        
    @property
    def vertex_list_1(self):
        return self._vertex_list_1
    
    @vertex_list_1.setter
    def vertex_list_1(self, vertices):
        
        self._vertex_list_check(vertices)
        
        self._vertex_list_1 = vertices
    
    @property
    def vertex_list_2(self):
        return self._vertex_list_2
    
    @vertex_list_2.setter
    def vertex_list_2(self, vertices):
        
        self._vertex_list_check(vertices)
        
        self._vertex_list_2 = vertices
        
    def check_for_similarity(self) -> bool:
        if not len(self.vertex_list_1) == len(self.vertex_list_2):
            return False
        if not self._check_side_proportions(self.vertex_list_1, self.vertex_list_2):
            return False
        
        #check for angles
        
        
    def _check_side_proportions(self, vertices_1, vertices_2):
        lenghts_1 = self._length_calc(vertices_1)
        lenghts_2 = self._length_calc(vertices_2)
        
        for rotation in range(len(lenghts_1)): #rotates one of the shapes and compare sides length
            rotated_vertices = lenghts_2[rotation:] + lenghts_2[:rotation]
            
            if rotated_vertices == 0: # avoids zero division error
                continue
            
            ratio = lenghts_1[0] / rotated_vertices[0]
            
            tolerance=1e-9 # avoids inconsistencies and innaccuracies in division
            
            if all(s2 != 0 and abs(s1 / s2 - ratio) < tolerance for s1, s2 in zip(lenghts_1, rotated_vertices)):
                #check for each possible variation
                return True
            
        return False
    
    def _length_calc(self, vertices):
        
        lengths = []
        for i in range((len(vertices) - 1)):
            
            lenght = ((vertices[i + 1][0] - vertices[i][0]) ** 2 + (vertices[i + 1][1] - vertices[i][1]) **2) ** 0.5
            lengths.append(lenght)
            
        lenght = ((vertices[0][0] - vertices[-1][0]) ** 2 + (vertices[0][1] - vertices[-1][1]) ** 2) ** 0.5
        lengths.append(lenght)
        
        return(lengths)
            
    
    def _vertex_list_check(self, vertices):
        if not isinstance(vertices, list):
            raise TypeError('Vertex List must be list object')
        if len(vertices) < 2:
            raise IndexError('Their must be atleast 3 vertices in the list')
        if not all(isinstance(i, (list, tuple)) and
                   len(i) == 2 and
                   all(isinstance(j, (int, float)) for j in i)for i in vertices):
            
            raise TypeError('Vertex List must contain only list or tuples, each of length 2 containing only int or float values')
        
        return vertices