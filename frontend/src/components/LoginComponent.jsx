import {useState, useEffect} from "react";
import '../assets/css/Login.css'

function LoginComponent() {
    const [formData, setFormData] = useState(
        {
            'username': '',
            'password': '',
        }
    )

    const handleChange = (e) => {
        const {id, value} = e.target
        setFormData(prev => ({...prev, [id]:value}))
    }

    const handleSubmit = async (e) => {
        e.preventDefault()

        const response = await fetch('http://127.0.0.1:8000/trophyhunters/token/',{
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(formData),
        })

        if (response.ok){
            const credentials = await response.json()
            localStorage.setItem('access', credentials.access)
            localStorage.setItem('refresh', credentials.refresh)
            alert(`Bienvenido ${formData.username}`)
        } else {
            const error = await response.json()
            alert(`${error.detail}`)
        }
    }

    return (
        <div className="container">
            <h1>LOGIN</h1>
            <form method="post" onSubmit={handleSubmit}>
                <label htmlFor="username">Username</label>
                <input type="text" id="username" onChange={handleChange}/>

                <label htmlFor="password">Password</label>
                <input type="password" id="password" onChange={handleChange}/>

                <button type="submit">Iniciar sesion</button>
            </form>
        </div>
    )
}

export default LoginComponent