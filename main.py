# Задача 1

class MinStat:
    def __init__(self):
        self.some_list = []

    def add_number(self, number):
        self.some_list.append(number)

    def result(self):
        if len(self.some_list) == 0:
            return None
        else:
            return min(self.some_list)


class MaxStat(MinStat):
    def result(self):
        if len(self.some_list) == 0:
            return None
        else:
            return max(self.some_list)


class AverageStat(MinStat):
    def result(self):
        if len(self.some_list) == 0:
            return None
        else:
            return sum(self.some_list) / len(self.some_list)



## Пример 1

# values = [1, 2, 4, 5]
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)
# print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))  ## Вывод: 1 5 3.000


## Пример 2

# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# print(mins.result(), maxs.result(), (average.result()))  ## Вывод: None None None

## Пример 3

# values = [1, 0, 0]
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()

# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)

# print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))  ## Вывод: 0 1 0.333



# Задача 2

class Table:
 
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.table = [[0] * cols for _ in range(rows)]
 
    def get_value(self, row, col):
        return (self.table[row][col] if 0 <= row < self.rows and 0 <= col < self.cols
                else None)
 
    def set_value(self, row, col, value):
        self.table[row][col] = value
 
    def n_rows(self):
        return self.rows
 
    def n_cols(self):
        return self.cols
 
    def delete_row(self, row):
        self.table.pop(row)
        self.rows -= 1
 
    def delete_col(self, col):
        for row in range(self.rows):
            self.table[row].pop(col)
        self.cols -= 1
 
    def add_row(self, row):
        self.table.insert(row, [0] * self.cols)
        self.rows += 1
 
    def add_col(self, col):
        for row in range(self.rows):
            self.table[row].insert(col, 0)
        self.cols += 1


# # Пример 1

# tab = Table(3, 5)
# tab.set_value(0, 1, 10) 
# tab.set_value(1, 2, 20)  
# tab.set_value(2, 3, 30) 

# for i in range (tab.n_rows()):                    ## Вывод: 0 10 0 0 0
#     for j in range (tab.n_cols()):                ##        0 0 20 0 0
#         print(tab.get_value(i, j), end=' ')       ##        0 0 0 30 0
#     print()
# print()

# tab.add_row(1)

# for i in range(tab.n_rows()):                      ## Вывод: 0 10 0 0 0
#     for j in range(tab.n_cols()):                  ##        0 0 0 0 0
#         print(tab.get_value(i , j), end=' ')       ##        0 0 0 20 0
#     print()                                        ##        0 0 0 30 0
# print()



# # Пример 2

# tab = Table(2, 2)
# for i in range (tab.n_rows()):                    ## Вывод: 0 0
#     for j in range (tab.n_cols()):                ##        0 0 
#         print(tab.get_value(i, j), end=' ')      
#     print()
# print()


# tab.set_value(0, 0, 10) 
# tab.set_value(0, 1, 20) 
# tab.set_value(1, 0, 30)  
# tab.set_value(1, 1, 40)  


# for i in range (tab.n_rows()):                    ## Вывод: 10 20
#     for j in range (tab.n_cols()):                ##        30 40
#         print(tab.get_value(i, j), end=' ')       
#     print()
# print()


# for i in range (-1, tab.n_rows() + 1):                    ## Вывод: None None None None
#     for j in range (-1, tab.n_cols() +1):                 ##        None 10 20 None
#         print(tab.get_value(i, j), end=' ')               ##        None 30 40 None
#     print()                                               ##        None None None None
# print()


# tab.add_row(0)
# tab.add_col(1)


# for i in range (-1, tab.n_rows() + 1):                    ## Вывод: None None None None None
#     for j in range (-1 ,tab.n_cols() + 1):                ##        None 0 0 0 None
#         print(tab.get_value(i, j), end=' ')               ##        None 10 0 20 None
#     print()                                               ##        None 30 0 40 None
# print()                                                   ##        None None None None None



# # Пример 3

# tab = Table(1, 1)

# for i in range(tab.n_rows()):                               ## Вывод: 0
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# tab.set_value(0, 0, 1000)

# for i in range(tab.n_rows()):                               ## Вывод: 1000
#     for j in range(tab.n_cols()):                           
#         print(tab.get_value(i, j), end=' ')                 
#     print()
# print()

# for i in range(-1, tab.n_rows() + 1):                       ## Вывод: None None None 
#     for j in range(-1, tab.n_cols() + 1):                   ##        None 1000 None 
#         print(tab.get_value(i, j), end=' ')                 ##        None None None 
#     print()                                                 
# print()                                                     

# tab.add_row(0)
# tab.add_row(2)
# tab.add_col(0)
# tab.add_col(2)

# tab.set_value(0, 0, 2000)
# tab.set_value(0, 2, 3000)
# tab.set_value(2, 0, 4000)
# tab.set_value(2, 2, 5000)

# for i in range(-1, tab.n_rows() + 1):                       ## Вывод: None None None None None
#     for j in range(-1, tab.n_cols() + 1):                   ##        None 2000 0 3000 None
#         print(tab.get_value(i, j), end=' ')                 ##        None 0 1000 0 None
#     print()                                                 ##        None 4000 0 5000 None
# print()                                                     ##        None None None None None
