from math import sqrt
from PIL import Image, ImageDraw
import numpy as np
"""
Assignment: Solve a Maze using Dijkstra's Algorithm

Objective:
In this assignment, you will implement Dijkstra's algorithm to find the shortest path in a maze represented as an RGB image. You will write custom data structures, including a PixelNode class and a priority queue, while ensuring efficient pathfinding.

Problem Description:
You are given an RGB image of a maze where:
- White pixels (all channels ≈ 255) represent valid paths.
- Non-white pixels (one or more channels < 255) represent obstacles.

Your goal is to find the shortest path between a start pixel and an end pixel, given their coordinates, by:
1. Converting the RGB maze image to a grayscale representation for simplicity.
2. Implementing a custom PixelNode class for maze pixels.
3. Building and utilizing a priority queue with a decrease_key operation for efficient pathfinding.
4. Using Dijkstra's algorithm to traverse the maze and determine the shortest path.

---

Tasks:

1. Grayscale Conversion
Write a function to convert the RGB maze image into grayscale using the formula:
  Gray = 0.2989 * R + 0.5870 * G + 0.1140 * B

Task:
Implement a function convert_to_grayscale(image) that:
- Takes the RGB image as input.
- Converts it to grayscale using the formula.
- Returns the grayscale image as a 2D array.

"""


# def convert_to_grayscale(image):
#     """
#     Convert an RGB image to grayscale.

#     :param image: Input RGB image as a 3D NumPy array
#     :return: Grayscale image as a 2D NumPy array
#     """
#     for i, row in enumerate(image):
#         for j, cell in enumerate(row):
#             R,G,B = cell
#             gray = 0.2989 * R + 0.5870 * G + 0.1140 * B
#             image[i][j] = int(gray)
#     print (image)
#     return image
    
def convert_to_grayscale(image):
    """
    Convert an RGB image to grayscale.

    :param image: Input RGB image as a 3D NumPy array
    :return: Grayscale image as a 2D NumPy array
    """
    # שימוש בפונקציות NumPy כדי לחשב את ערכי גווני האפור
    grayscale = 0.2989 * image[:, :, 0] + 0.5870 * image[:, :, 1] + 0.1140 * image[:, :, 2]
    
    # המרה לערכים שלמים (למטרת תמונה בגווני אפור)
    grayscale = grayscale.astype(np.uint8)
    
    return grayscale

"""
2. Pixel Representation
Create a class PixelNode to represent each pixel in the maze. It should include:
- x and y: Coordinates of the pixel.
- distance: Shortest known distance from the start pixel (initialize to infinity).
- visited: Boolean indicating whether the pixel has been processed.
- color: Optional attribute for the grayscale intensity value.
- heap_index: The index of the PixelNode in the priority queue. This is essential for efficient decrease_key operations.

Additionally:
- Implement comparison operators (e.g., _lt_) to make PixelNode objects compatible with a min-heap.

"""


class PixelNode:
    def __init__(self, x, y, color=None):
        """
        Initialize a PixelNode object.

        :param x: X-coordinate of the pixel
        :param y: Y-coordinate of the pixel
        :param color: Grayscale intensity of the pixel
        """
        self.x = x
        self.y = y
        self.color = color
        self.distance = float('inf')
        self.visited = False
        self.heap_index = None
        self.prev = None

    def _distance(self, other):
        x1, y1 = self.x, self.y
        x2, y2 = other.x, other.y
        return sqrt((x1-x2)*2 + (y1-y2)*2)
        

    def __lt__(self, other):
        """
        Comparison operator for PixelNode based on distance.
        """
        return self.distance < other.distance
    
    def __gt__(self, other):
        """
        Comparison operator for PixelNode based on distance.
        """
        return self.distance > other.distance


"""
3. Priority Queue
Write a class PriorityQueue for managing PixelNode objects. Use a min-heap for efficient operations. Include the following methods:
- insert(node): Add a new PixelNode to the queue and update its heap_index.
- extract_min(): Remove and return the PixelNode with the smallest distance while maintaining the heap property.
- decrease_key(node, new_distance): Update the distance of an existing node and adjust its position in the heap. Update its heap_index.

Hint:
Use the heap_index attribute of PixelNode objects to keep track of their position in the heap. This allows decrease_key to access nodes efficiently.
"""

class PriorityQueue:
    @staticmethod
    def left_child(i):
        return (i*2)+1 
    
    @staticmethod
    def right_child(i):
        return (i*2)+2
    
    @staticmethod
    def father(i):
        return (i-1)//2
    

    def __init__(self):
        """
        Initialize an empty priority queue.
        """
        self.queue = []

    def insert(self, node):
        """
        Insert a PixelNode into the priority queue.

        :param node: The PixelNode to be inserted
        """
        self.queue.append(node)
        node_i = len(self.queue)-1
        node.heap_index = node_i
        self.heapify_up(node_i)
    
    def heapify_up(self, i):
        father_i = PriorityQueue.father(i)
        while i > 0 and self.queue[i] < self.queue[father_i]:
            self.queue[father_i].heap_index , self.queue[i].heap_index = i, father_i
            self.queue[father_i], self.queue[i] = self.queue[i], self.queue[father_i]
            i = father_i
            father_i = PriorityQueue.father(i)
        
        return i 


    def extract_min(self):
        """
        Extract and return the PixelNode with the smallest distance.

        :return: The PixelNode with the smallest distance
        """
        if not self.queue:
            return 
        self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
        self.queue[0].heap_index = 0
        min = self.queue.pop()
        self.heapify_down(0)
        return min
    
    def heapify_down(self, i):
        heap_len = len(self.queue)
        left_child = PriorityQueue.left_child(i)
        while left_child < heap_len:
            minimum = i
            if self.queue[i] > self.queue[left_child]:
                minimum = left_child
            right_child = PriorityQueue.right_child(i)
            if right_child < heap_len and self.queue[right_child] < self.queue[minimum]:
                minimum = right_child

            if minimum == i:
                break

            self.queue[i].heap_index, self.queue[minimum].heap_index = minimum , i
            self.queue[i], self.queue[minimum] = self.queue[minimum], self.queue[i]
            i = minimum
            left_child = PriorityQueue.left_child(i)
        
        return i 

    def decrease_key(self, node, new_distance):
        """
        Update the distance of a node and reheapify.

        :param node: The PixelNode whose distance is to be updated
        :param new_distance: The new distance value
        """
        node.distance = new_distance
        node_i = node.heap_index
        node_i = self.heapify_up(node_i)
        self.heapify_down(node_i)


    def neighbors(self, node, matrix):
        x, y = node.x, node.y
        neighbors_list = []
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # בדיקה שאנחנו בתוך גבולות המטריצה
            if (0 <= new_y < len(matrix) and 
                0 <= new_x < len(matrix[0])):
                
                neighbor = matrix[new_y][new_x]  # שים לב לסדר: קודם y ואז x
                # בדיקה שהשכן הוא פיקסל לבן ושלא ביקרנו בו
                if not neighbor.visited and neighbor.color > 200:
                    neighbors_list.append(neighbor)  # מחזירים את אובייקט ה-PixelNode
        
        return neighbors_list
    

"""
4. Dijkstra's Algorithm
Implement Dijkstra's algorithm to find the shortest path from the start pixel to the end pixel.
"""
    

def dijkstra(gray_image_matrix, start, end, BOUNDARY = 200):
    # יצירת מטריצת הצמתים - שים לב לסדר הנכון של x,y
    pixel_nodes_matrix = [
        [PixelNode(x, y, cell) for x, cell in enumerate(row)]
        for y, row in enumerate(gray_image_matrix)
    ]

    # הגדרת צומת ההתחלה
    start_x, start_y = start
    start_node = pixel_nodes_matrix[start_y][start_x]  # שים לב לסדר: y ואז x
    start_node.distance = 0

    # הגדרת צומת הסיום
    end_x, end_y = end
    end_node = pixel_nodes_matrix[end_y][end_x]  # שים לב לסדר: y ואז x

    queue = PriorityQueue()
    queue.insert(start_node)

    while queue.queue:
        temp = queue.extract_min()
        if temp is None:  # אם התור ריק
            break
            
        temp.visited = True
        
        # בדיקה אם הגענו ליעד
        if temp is end_node:
            print("found")
            break
            
        neighbors = queue.neighbors(temp, pixel_nodes_matrix)
        for neighbor in neighbors:
            new_distance = temp.distance + 1
            if new_distance < neighbor.distance:
                neighbor.distance = new_distance
                neighbor.prev = temp
                
                if neighbor.heap_index is not None:
                    queue.decrease_key(neighbor, new_distance)
                else:
                    queue.insert(neighbor)

    # שחזור המסלול
    path = []
    current = end_node
    while current is not None:
        path.append((current.x, current.y))
        current = current.prev

    path.reverse()
    return path

def main():
    image_path = "C:\mefathim\graph\mazes\maze5.jpg"
    image = Image.open(image_path)
    start = (212, 289) 
    end = (1430, 1964)
    image = draw_diagonal_lines(image, start, end, thickness=3, color=(0, 0, 0))
    rgb_image = np.array(image)
    gray_image = convert_to_grayscale(rgb_image)
    image.show()

   
    path = dijkstra(gray_image, start, end)
    print(path)
   
    
    # Draw the path with thicker lines and more visible color
    draw = ImageDraw.Draw(image)
    
    # Draw path segments as lines instead of points
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        # Draw a line between consecutive points
        draw.line([(x1, y1), (x2, y2)], fill=(255, 0, 0), width=10)
    
    # Highlight start and end points
    start_point_size = 5
    draw.ellipse([start[0] - start_point_size, start[1] - start_point_size, 
                  start[0] + start_point_size, start[1] + start_point_size], 
                 fill=(0, 255, 0))  # Green for start
    draw.ellipse([end[0] - start_point_size, end[1] - start_point_size, 
                  end[0] + start_point_size, end[1] + start_point_size], 
                 fill=(255, 0, 0))  # Red for end

    image.show()

def draw_diagonal_lines(image, start, end, thickness=1, color=(0, 0, 0)):
    """
    Draw diagonal lines from the start and end points to block paths outside the maze.

    :param image: Input PIL image (RGB)
    :param start: Starting point (x, y) of the maze
    :param end: Ending point (x, y) of the maze
    :param thickness: Thickness of the lines
    :param color: Color of the lines (default: black)
    """
    draw = ImageDraw.Draw(image)
    width, height = image.size

    # קווים מנקודת הכניסה
    start_x, start_y = start
    draw.line([(start_x-1, start_y-1), (0, 0)], fill=color, width=thickness)  # קו אלכסוני לפינה העליונה השמאלית
    draw.line([(start_x+1, start_y+1), (width, 0)], fill=color, width=thickness)  # קו אלכסוני לפינה העליונה הימנית

    # קווים מנקודת היציאה
    end_x, end_y = end
    draw.line([(end_x-1, end_y-1), (0, height)], fill=color, width=thickness)  # קו אלכסוני לפינה התחתונה השמאלית
    draw.line([(end_x+1, end_y+1), (width, height)], fill=color, width=thickness)  # קו אלכסוני לפינה התחתונה הימנית

    return image


main()




