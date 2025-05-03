import {Link} from "react-router-dom";

function NavComponent() {

    return (
        <header>
          <nav>
            <ul>
              <li>
                <Link to="trophyhunters/register">Registro</Link>
              </li>
              <li>
                <Link to="trophyhunters/login">Login</Link>
              </li>
            </ul>
          </nav>
        </header>
    )
}


export default NavComponent