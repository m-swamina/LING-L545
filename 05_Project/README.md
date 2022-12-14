# Project


Named Entity Recognition is the task in Natural Lan-
guage Processing (NLP) that has its real world ap-
plication growing in every field. The purpose of this
project is to build a dialogue system that converses
with the user agent by asking questions for collect-
ing information on flight ticketing. Given a dialogue
from the user agent Named Entity Recognition us-
ing BERT is performed. BERT is a language model
that relies on a transformer which is bidirectionally
trained which allows augments a greater sense of con-
text in language compared to other models. An entity
is a word or group of words that belong to a particu-
lar category like location, organization, etc. The next
step after detecting an entity and categorizing the en-
tity, is to fed it into the dialogue system to form a
question for the dialogue agent. This is implemented
with the inspiration of hybrid architecture and frame
based architecture. The necessary responses from
the user is stored in frames or slots. These slots or
frames are used to perform a certain goal or task like
finding available flights based on the user’s input. In
this project a part of the dialogue system is imple-
mented. Once the user response is fed into the NER
model which acts as Natural Language Understand-
ing component of the dialogue system architecture.
Some rules are created based on the output of the
NER model to store the information from the user.
The agent dialogues is prompted by rules based on
the design of the conversation flow. The BERT model
for Named Entity Recognition is trained on two dif-
ferent optimizers Adam and Stochastic Gradient De-
scent (SGD), and the accuracies are compared. The
BERT using SGD performs the best with an accu-
racy of 97.8% and the BERT using Adam results in
accuracy of 86.3% .
