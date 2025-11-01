from math import atan2, pi

class VertexCheck:
    """
    A CLass that checks the relation between two objects
    """
    def __init__(self, list_of_vertices_shape_one: list,
                 list_of_vertices_shape_two: list):
        """
        Initializes the Class
        Args:
            list_of_vertices_shape_one (list): List of Coordinates of first shape
            list_of_vertices_shape_two (list): List of Coordinates of second shape
        """
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
        """
        Check if the No. of Sides and Angles are Same and Length of sides are Proportional
        Returns:
            bool: Returns True if similar and False otherwise
        """
        if not len(self.vertex_list_1) == len(self.vertex_list_2):
            return False
        if not self._check_side_proportions(self.vertex_list_1, self.vertex_list_2):
            return False
        
        return True
    
        
    def _check_side_proportions(self, vertices_1, vertices_2):
        """
        check for side and angles
        Args:
            vertices_1 (list): coordinates of first shape
            vertices_2 (list): coordinates of second shape

        Returns:
            bool: Return True only if Sides Proportional and Angles Same
        """
        lenghts_1 = self._length_calc(vertices_1)
        lenghts_2 = self._length_calc(vertices_2)
        
        angles_1 = self._calculate_interior_angles(vertices_1)
        angles_2 = self._calculate_interior_angles(vertices_2)
        
        tolerance_side = 1e-9 # avoids inconsistencies and innaccuracies in division
        tolerance_angle = 1e-6
        
        for rotation in range(len(lenghts_1)): #rotates one of the shapes and compare sides length
            rotated_vertices = lenghts_2[rotation:] + lenghts_2[:rotation]
            rotated_angles = angles_2[rotation:] + angles_2[:rotation]

            
            if rotated_vertices[0] == 0: # avoids zero division error
                continue
            
            ratio = lenghts_1[0] / rotated_vertices[0]
            
            
            are_side_proportional = all(s2 != 0 and abs(s1 / s2 - ratio) < tolerance_side for s1, s2 in zip(lenghts_1, rotated_vertices))            
            are_angles_equal = all(abs(a1 - a2) < tolerance_angle for a1, a2 in zip(angles_1, rotated_angles))
            #check for each possible variation

            if are_side_proportional and are_angles_equal:
                return True
            
        return False
    
    def _length_calc(self, vertices):
        """
        Calculates the lenghts of all sides
        Args:
            vertices (list): coordinates of shapes
        
        Returns:
            list: Returns list of lengths 
        """
        
        lengths = []
        for i in range((len(vertices) - 1)):
            
            lenght = ((vertices[i + 1][0] - vertices[i][0]) ** 2 + (vertices[i + 1][1] - vertices[i][1]) **2) ** 0.5
            lengths.append(lenght)
            
        lenght = ((vertices[0][0] - vertices[-1][0]) ** 2 + (vertices[0][1] - vertices[-1][1]) ** 2) ** 0.5
        lengths.append(lenght)
        
        return(lengths)

    def _calculate_interior_angles(self, vertices):
        """
        Calculates the interior angle for all sides
        Args:
            vertices (list): list of coordinates 

        Returns:
            list: List of angles
        """
        angles = []
        n = len(vertices)
        
        for i in range(n):
            # Get three consecutive points
            p1 = vertices[(i - 1) % n]  # Previous vertex
            p2 = vertices[i]             # Current vertex
            p3 = vertices[(i + 1) % n]   # Next vertex
            
            # Create vectors from current vertex to neighbors
            v1x = p1[0] - p2[0]
            v1y = p1[1] - p2[1]
            v2x = p3[0] - p2[0]
            v2y = p3[1] - p2[1]
            
            # Calculate angles of each vector
            angle1 = atan2(v1y, v1x)
            angle2 = atan2(v2y, v2x)
            
            # Calculate interior angle
            angle = angle2 - angle1
            
            # Normalize to [0, 2π]
            while angle < 0:
                angle += 2 * pi
            while angle > 2 * pi:
                angle -= 2 * pi
            
            # For interior angle, use the smaller angle if > π
            if angle > pi:
                angle = 2 * pi - angle
                
            angles.append(angle)
        
        return angles
            
    
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