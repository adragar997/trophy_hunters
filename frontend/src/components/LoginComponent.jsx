import {useState, useEffect} from "react";

function LoginComponent() {
    const user = {
        'username': '',
        'password': '',
    }

    const setUsername = (e) => {
        user.username = e.target.value
    }

    const setPassword = (e) => {
        user.password = e.target.value
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        console.log(user)
    }

    return (
        <div>
            <h1>LOGIN</h1>
            <form method="post" onSubmit={handleSubmit}>
                <label htmlFor="username">Username</label>
                <input type="text" id="username" onChange={setUsername}/>

                <label htmlFor="password">Password</label>
                <input type="text" id="password" onChange={setPassword}/>

                <button type="submit">Iniciar sesion</button>
            </form>
        </div>
    )
}

export default LoginComponent