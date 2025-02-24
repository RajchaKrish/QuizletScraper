from selenium.webdriver import Chrome


if __name__ == "__main__":
  site = input("Paste the link to the NOTECARDS of the quizlet site. eg https://quizlet.com/146556235/flashcards  ")
  
  driver = Chrome()
  driver.get(site)
  
  
  driver.quit()
