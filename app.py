from flask import Flask,request,render_template
from get_recipes import get_recs
import requests  
from bs4 import BeautifulSoup  

def getdata(url):
        r = requests.get(url)
        r.raise_for_status() 
        return r.text
head="https://www.archanaskitchen.com"
def get_image(url):
      htmldata=getdata(url)
      soup = BeautifulSoup(htmldata, 'html.parser')
      images=soup.find_all('img',class_='img-fluid img-thumbnail')
      #image_url = [head + img['src'] for img in images]
      return head+images[0]['src']

app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route("/recommend",methods=['POST'])
def recommend():
    if request.method == 'POST':
      ingrd = request.form.get("ingredients")
      recipes=get_recs(ingrd)
      recipes['image-url']=recipes['URL'].apply(get_image)
      recipe=recipes[['TranslatedRecipeName','image-url','URL']]
      #table_html = recipes.to_html(classes='table table-bordered', index=False)
      recipe_list = recipe.to_dict(orient='records')
      return render_template('index.html',recipe_list=recipe_list)
    else:
        return render_template('index.html')
    
if __name__=='__main__':
   app.run(debug=True)

