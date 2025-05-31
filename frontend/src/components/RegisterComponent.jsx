import {useState, useEffect} from "react";
import '../assets/css/Register.css';

function RegisterComponent() {
    const [formData, setFormData] = useState(
            {
            'username': '',
            'password':'',
            'avatar':null,
            'banner':null,
            'bio': '',
            'firstname': '',
            'lastname': '',
            'birthdate': ''
        }
    )

    const handleSubmit = async (e) => {
        e.preventDefault()
        const payload = new FormData();

        payload.append("username",  formData.username);
        payload.append("password",  formData.password);
        payload.append("avatar",  formData.avatar);
        payload.append("banner",  formData.banner);
        payload.append("bio",       formData.bio);
        payload.append("firstname", formData.firstname);
        payload.append("lastname",  formData.lastname);
        payload.append("birthdate", formData.birthdate);

        const response = await fetch('http://127.0.0.1:8000/trophyhunters/register/',{
            method: "POST",
            body: payload,
        })

        const data = await response.json()
        console.log(data)
    }

    const handleChange = (e) => {
        const {id, value} = e.target
        setFormData(prev => ({...prev, [id]:value}))
    }

    const handleImage = (e) => {
        const {id, files} = e.target
        setFormData(prev => ({ ...prev, [id]: files[0] }));
    }

    return (
        <div className='container'>
            <h1>Formulario de registro</h1>
            <form method="post" onSubmit={handleSubmit}>
                <label htmlFor="username">Usuario</label>
                <input type="text" id="username" name="username" onChange={handleChange}/>

                <label htmlFor="password">Contraseña</label>
                <input type="password" id="password" name="password" onChange={handleChange}/>

                <label htmlFor="avatar">Foto de avatar</label>
                <input type="file" id="avatar" name="avatar" onChange={handleImage}/>

                <label htmlFor="banner">Banner</label>
                <input type="file" id="banner" name="banner" onChange={handleImage}/>

                <label htmlFor="bio">Sobre mi</label>
                <textarea id="bio" cols="30" rows="10" name="bio" onChange={handleChange}></textarea>
                
                <label htmlFor="firstname">Nombre</label>
                <input type="text" id="firstname" name="firstname" onChange={handleChange}/>

                <label htmlFor="lastmame">Apellidos</label>
                <input type="text" id="lastname" name="lastname" onChange={handleChange}/>

                <label htmlFor="birthdate">Cumpleaños</label>
                <input type="date" id="birthdate" name="birthdate" onChange={handleChange}/>

                <button type="submit">Registrarse</button>
            </form>
        </div>
    )
}

export default RegisterComponent