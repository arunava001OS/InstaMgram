import base from 'axios'
import {useState,setState} from 'react'
import './css/app.css'
import Authform from './components/authform'
function App() {

  const [isLoggedIn,setIsLoggedIn] = useState(false)
  
  if (isLoggedIn) {
    return (
      <div className="app__loggedin">
        <h1>LoggedIn</h1>
      </div>
    );
  }else{
    return (
      <div className="app__loggedout">
        <h1>LoggedOut</h1>
        <Authform setIsLoggedIn={setIsLoggedIn}></Authform>
        
      </div>
    );
  }
  
}

export default App;
