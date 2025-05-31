import {useState, useEffect} from "react";
import { useNavigate } from 'react-router-dom';
import '../assets/css/Login.css'

function LoginComponent(props) {
    const [formData, setFormData] = useState(
        {
            'username': '',
            'password': '',
        }
    )
    const navigate = useNavigate()


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

            props.setUser(
                {'username':formData.username}
            )
            navigate('/trophyhunters/register')
        } else {
            const error = await response.json()
            alert(`${error.detail}`)
        }
    }

    return (
        <div className="flex justify-center items-center min-h-screen bg-main-page">
            <div className="bg-white p-8 rounded-lg w-96">
                <h1 className="text-2xl text-center mb-6">LOGIN</h1>
                <form method="post" onSubmit={handleSubmit}>
                    <div className="mb-4">
                        <label htmlFor="username" className="block">Username</label>
                        <input type="text" id="username" className="input" onChange={handleChange}/>
                    </div>

                    <div className="mb-6">
                        <label htmlFor="password" className="block">Password</label>
                        <input type="password" id="password" className="input" onChange={handleChange}/>
                    </div>

                    <button type="submit"
                            className="w-fit block py-2 px-4 bg-blue-700 text-white focus: rounded-lg">Iniciar sesion
                    </button>
                    <div className="block justify-center mt-4 mb-2">
                        <hr/>
                    </div>
                </form>
            </div>
        </div>
    )
}

export default LoginComponent