import app from "firebase/app";
import "firebase/database";
import "firebase/storage";
import "firebase/auth";

let firebaseConfig = {
  apiKey: "AIzaSyDOYJEfoxpNko2gum16qUo3Uf1e7qfV-KA",
  authDomain: "juntoseguros-todolist.firebaseapp.com",
  projectId: "juntoseguros-todolist",
  databaseURL: "https://juntoseguros-todolist-default-rtdb.firebaseio.com/",
  storageBucket: "juntoseguros-todolist.appspot.com",
  messagingSenderId: "330907459321",
  appId: "1:330907459321:web:458d26e7618e78289c0c28"
 };

class Firebase{
  constructor(){
    app.initializeApp(firebaseConfig);

    this.app = app.database();
  }

  cadastra(email, senha){
    app.auth().createUserWithEmailAndPassword(email, senha)
    .then(data => {
      let chave = data.user.uid;
    })
    .catch((error) => {
      if(error.code === "auth/invalid-email"){
        alert("Endereço de e-mail inválido");
      }
      else if(error.code === "auth/weak-password"){
        alert("A senha não atinge os requisitos de segurança");
      }
      else if(error.code === "auth/email-already-in-use"){
        alert("E-mail \"" + email + "\" já está em uso, por favor utilize outro e-mail");
      }
      else{
        alert("Erro: " + error.code);
      }
    });
  }
}

export default new Firebase();
