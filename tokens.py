class Game_Tokens:

  def __init__(self, color, value, face):
    self.color = color
    self.value = value
    self.face = face

#WIP can change the desc any time idc
 
  def token_desc(self):
    REG = "\033[38;5;232m"
    print(REG +
        f"You get a mysertious coin with a {self.color} hue. On the front is a picture of {self.face} and on the back is a large enscripted {self.value}."
    )

#can change value statements when we decide how coins/ token work :)

  def token_value(self):
    if self.value == 1:
      print("(Hmm.. This coin must not be worth much.)")
    elif self.value == 5:
      print("(Oh this coin's worth a fair amount. Better hang onto this.)")
    elif self.value == 10:
      print("(Wow! Must be my lucky day!)")


#smth abt face idrk

  def token_face(self):
    if self.face == "Cecil":
      print("(Huh.. It's Cecil. Guess he wasn't bluffing about those tokens)")
    elif self.face == "Claire":
      print("(Claire? That's odd, I can't find her anywhere. Oh. Well, I'm glad she got to move on)")
    elif self.face == "Vera":
      print("(I wonder what she meant by that)")