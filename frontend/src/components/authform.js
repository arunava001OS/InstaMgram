import React from 'react'
import base from '../axios'
function Authform() {

    return (
        <div className="app__form">
          <div className="app__signup">
            <h1>SIGNUP</h1>
            <form>
                <label>Username</label>
                <input type="text" name="username"></input> <br></br>
                <label>Email</label>
                <input type="text" name="email"></input> <br></br>
                <label>Password</label>
                <input type="password" name="password"></input> <br></br>
                <label> Confirm Password</label>
                <input type="password" name="password2"></input> <br></br>
                <button>Signup</button>
            </form>
          </div>
          <div className="app__login">
            <h1>LOGIN</h1>
            <label>Username</label>
            <input type="text" name="username"></input> <br></br>
            <label>Password</label>
            <input type="password" name="password"></input> <br></br>
            <button>Login</button>
          </div>
        </div>
    )
}

export default Authform;
