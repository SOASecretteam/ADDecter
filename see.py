from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.facebook.com/v2.8/plugins/post.php?app_id=&channel=https%3A%2F%2Fstaticxx.facebook.com%2Fconnect%2Fxd_arbiter%2Fr%2FtrnHszv6jVd.js%3Fversion%3D42%23cb%3Df53ef301a4d504%26domain%3Dadespresso.com%26origin%3Dhttps%253A%252F%252Fadespresso.com%252Ff152fc5e2a9b73c%26relation%3Dparent.parent&container_width=728&href=https%3A%2F%2Ffacebook.com%2F324826532457%2Fposts%2F10156791151362458&locale=en_US&sdk=joey&width=600'
#driver = webdriver.PhantomJS(executable_path=r'C:/Users/Lynn/Desktop/SOA/phantomjs-2.1.1-windows/bin/phantomjs.exe')  # PhantomJs

driver = webdriver.Chrome()
driver.get(url)
pageSource = driver.page_source

soup = BeautifulSoup(url, "html.parser")
soup
Like_box = soup.find("div",attrs={"class":"_2pi4 _36iq _4lk2 _3xre _2165"})
Like_box
company_box = soup.find("div",attrs={"class":"_2_79 _50f4 _50f7"})
company_box
image_box = soup.find("img",attrs={"class":"scaledImageFitWidth img"})
print(image_box)
for a in image_box:
    print (a)
    if a.img:
        print(a.img["src"])

Like = Like_box.text.split()
Like
company = company_box.text.split()
image = image_box.text.split()
print(Like)
print(company)
print(image_box)


driver.close()

#<div class="_2pi4 _36iq _4lk2 _3xre _2165" title="Like"><i class="_3-8_ _2yf7 _5jp _2166 img sp_post-plugin sx_post-plugin_like-light"></i><i class="_3-8_ _2yf7 _3wdt _2166 img sp_post-plugin sx_post-plugin_like"></i>27</div>
#<img class="scaledImageFitWidth img" src="https://scontent-tpe1-1.xx.fbcdn.net/v/t45.1600-4/cp0/q90/s600x600/42506390_23843113879740035_5894572236978782208_n.png.jpg?_nc_cat=101&amp;efg=eyJxZV9ncm91cHMiOlsibm9fc2FmZV9pbWFnZV9mb3JfYWRzX2ltYWdlIl19&amp;oh=44fb05ce487dde37c9db27eebdaac7b2&amp;oe=5C4BFA6A" style="top:0px;" alt="" width="598" height="313" data-ad-preview="image" aria-label="Image may contain: one or more people, indoor and text">