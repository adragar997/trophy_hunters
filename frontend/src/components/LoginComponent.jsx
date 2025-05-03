import {useState, useEffect} from "react";

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

    const handleSubmit = (e) => {
        e.preventDefault()
        console.log(formData)
    }

    return (
        <div>
            <h1>LOGIN</h1>
            <form method="post" onSubmit={handleSubmit}>
                <label htmlFor="username">Username</label>
                <input type="text" id="username" onChange={handleChange}/>

                <label htmlFor="password">Password</label>
                <input type="text" id="password" onChange={handleChange}/>

                <button type="submit">Iniciar sesion</button>
            </form>
        </div>
    )
}

export default LoginComponent