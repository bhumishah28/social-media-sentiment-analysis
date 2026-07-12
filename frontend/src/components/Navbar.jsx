import { useState } from "react";

function Navbar() {

    const [active, setActive] = useState("Home");

    return (

        <nav className="navbar">

            <div className="logo">

                SentimentScope

            </div>

            <ul className="nav-links">

                <li>

                    <a
                        href="#"
                        className={
                            active === "Home"
                            ? "active"
                            : ""
                        }
                        onClick={() =>
                            setActive("Home")
                        }
                    >
                        Home
                    </a>

                </li>

                <li>

                    <a
                        href="#analytics"
                        className={
                            active === "Analytics"
                            ? "active"
                            : ""
                        }
                        onClick={() =>
                            setActive("Analytics")
                        }
                    >
                        Analytics
                    </a>

                </li>

                <li>

                    <a
                        href="#history"
                        className={
                            active === "History"
                            ? "active"
                            : ""
                        }
                        onClick={() =>
                            setActive("History")
                        }
                    >
                        History
                    </a>

                </li>

            </ul>

            <button
                className="nav-btn"
                onClick={() => {

                    document
                        .querySelector("textarea")
                        ?.scrollIntoView({
                            behavior: "smooth",
                        });

                }}
            >

                Start Analysis

            </button>

        </nav>

    );

}

export default Navbar;