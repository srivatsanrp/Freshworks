# Freshworks
JSON-Merge

# It merge a series of files containing JSON array of Objects into a single file containing one JSON object.
# Prerequisites
   
     Python 
     PyPi
   
# Installation
    
    sudo apt install python
    pip install docopt==0.6.2
    python get-pip.py
  
Example:

$ cat > a.json
   
     {
      "a": {
        "name": "Alexis Sanchez", 
        "club": "Manchester United"
    },
    
    "b": {
        "name": "Robin van Persie",
        "club": "Feyenoord" ,
        "nested": {
            "a": 1,
            "b": 2
        }
    }
  }

$ cat > b.json
   
      {
      "a": {
        "name": "Nicolas Pepe", 
        "club": "Arsenal" 
    },
 
        "nested": {
            "a": 10
        }
    }

$ cat > c.json
   
     {
      "a": {
          "name": "Gonzalo Higuain", "club": "Napoli", 
          "name": "Sunil Chettri", "club": "Bengaluru FC" 
    },
 
          "nested": {
          "a": 10
        }
    }
 
 $ python jsonmerge.py a.json b.json c.json
 
     {
     "a":
        {
        "club": "Bengaluru FC", 
        "name": "Sunil Chettri"
        }, 
     "b":
     {
     "club": "Feyenoord", "name": "Robin van Persie", "nested": {"a": 1, "b": 2}},
        { 
     "name": "Gonzalo Higuain", "club": "Napoli" }
     "nested": {"a": 10}
     }
     
