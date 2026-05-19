text = "968-Maria, ( D@t@ Engineer );; 27 y  "

text = text.strip()

ni = text[0:3]
name = text[4:9]
role = text[13:26].replace("@", "a")
age = text[-4:]

print(f"Number Indetity : {ni}, Name {name}, role : {role}, age : {age}ears")
