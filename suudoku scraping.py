from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.sudokuweb.org/')
sudoku=driver.find_element(By.ID,'sudoku')
sudoku_squares=[]

def sudoku_scraper():
    for i in range(0, 81, 1):
        if i != 0:
            try:
                sudoku_square_visible = sudoku.find_element(By.ID, f'right{i}').find_element(By.CLASS_NAME, 'sedy').text
            except:
                sudoku_square_visible = 0
            sudoku_squares.append(str(sudoku_square_visible))
        else:
            try:
                sudoku_square_visible = sudoku.find_element(By.ID, f'right').find_element(By.CLASS_NAME, 'sedy').text
            except:
                sudoku_square_visible = 0
            sudoku_squares.append(str(sudoku_square_visible))
    print(f"I'm the unsolved sudoku squares: {''.join(sudoku_squares)}")
    solve_sudoku = driver.find_element(By.CLASS_NAME, 'oplossing')
    solve_sudoku.click()
    sudoku_squares.clear()
    for j in range(0, 81, 1):
        if j != 0:
            # sudoku_square = sudoku.find_element(By.ID, f'right{j}')
            try:
                sudoku_square_visible = sudoku.find_element(By.ID, f'right{j}').find_element(By.CLASS_NAME, 'sedy').text
            except:
                sudoku_square_visible = sudoku.find_element(By.ID, f'right{j}').find_element(By.CLASS_NAME, 'show').text
            sudoku_squares.append(str(sudoku_square_visible))
        else:
            # sudoku_square = sudoku.find_element(By.ID, f'right')
            try:
                sudoku_square_visible = sudoku.find_element(By.ID, f'right').find_element(By.CLASS_NAME, 'sedy').text
            except:
                sudoku_square_visible = sudoku.find_element(By.ID, f'right').find_element(By.CLASS_NAME, 'show').text
            sudoku_squares.append(str(sudoku_square_visible))
    print(f"I'm the solved sudoku squares: {''.join(sudoku_squares)}")
    sudoku_squares.clear()
for p in range(30):
    sudoku_scraper()
    driver = webdriver.Chrome()
    driver.get('https://www.sudokuweb.org/')
    sudoku = driver.find_element(By.ID, 'sudoku')