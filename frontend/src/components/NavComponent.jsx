import {Link} from "react-router-dom";

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
                            <Link to="trophyhunters/register">Registro</Link>
                        </li>
                        <li>
                            <Link to="trophyhunters/login">Login</Link>
                        </li>
                    </ul>
                }
          </nav>
        </header>
    )
}


export default NavComponent