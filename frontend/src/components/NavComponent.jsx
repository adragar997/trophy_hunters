import {Link} from "react-router-dom";
import '../assets/css/Navbar.css'

function NavComponent(props) {
    const {user} = props
    return (
        <header>
          <nav>
                {user ?
                    <ul>
                        <li>Bienvenido {user.username}</li>
                    </ul>
                    :
                    <div className="flex justify-between">
                        <Link to="/register">Registro</Link>
                        <Link to="/login">Login</Link>
                    </div>
                }
          </nav>
        </header>
    )
}


export default NavComponent