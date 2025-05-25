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
                    <ul>
                        <li>
                            <Link to="/register">Registro</Link>
                        </li>
                        <li>
                            <Link to="/login">Login</Link>
                        </li>
                    </ul>
                }
          </nav>
        </header>
    )
}


export default NavComponent