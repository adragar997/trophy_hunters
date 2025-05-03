import {useState, useEffect} from "react";

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

    const handleSubmit = (e) => {
        e.preventDefault()
        console.log(formData)
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
        <div>
            <h1>Formulario de registro</h1>
            <form method="post" onSubmit={handleSubmit}>
                <label htmlFor="username">Usuario</label>
                <input type="text" id="username" onChange={handleChange}/>

                <label htmlFor="password">Foto de avatar</label>
                <input type="password" id="password" onChange={handleChange}/>

                <label htmlFor="avatar">Foto de avatar</label>
                <input type="file" accept="image/*" id="avatar" onChange={handleImage}/>

                <label htmlFor="banner">Banner</label>
                <input type="file" accept="image/*" id="banner" onChange={handleImage}/>

                <label htmlFor="bio">Sobre mi</label>
                <textarea id="bio" cols="30" rows="10" onChange={handleChange}></textarea>
                
                <label htmlFor="firstname">Nombre</label>
                <input type="text" id="firstname" onChange={handleChange}/>

                <label htmlFor="lastmame">Apellidos</label>
                <input type="text" id="lastname" onChange={handleChange}/>

                <label htmlFor="birthdate">Cumpleaños</label>
                <input type="date" id="birthdate" onChange={handleChange}/>

                <button type="submit">Registrarse</button>
            </form>
        </div>
    )
}

export default RegisterComponent