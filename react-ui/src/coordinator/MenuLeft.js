import {Card, ListGroup} from "react-bootstrap";
import {useNavigate} from "react-router-dom";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import React from "react";
import {faMap} from "@fortawesome/free-solid-svg-icons/faMap";

const MenuLeft = () => {
    const navigate = useNavigate();

    return (
        <>
            <Card style={{width: '18rem'}}>
                <Card.Body>
                    <FontAwesomeIcon icon={faMap}
                                     className="new-icon mt-1 d-none d-md-block "
                                     onClick={() => navigate('/R/map')}
                                     fixedWidth/>
                </Card.Body>
            </Card>
        </>
    )
}

export default MenuLeft