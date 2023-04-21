import React, { useContext } from "react";
import { format } from "timeago.js";
import { LikeFilled, CommentOutlined, LikeOutlined } from "@ant-design/icons";
import { Link } from "react-router-dom";
import { Image, Card, Dropdown } from "react-bootstrap";
import axiosService from "../../helpers/axios";
import { getUser } from "../../hooks/user.actions";
import UpdateOffer from "./UpdateOffer";
import { Context } from "../Layout";
import MoreToggleIcon from "../MoreToggleIcon";

function Offer(props) {
  const { offer, refresh, isSingleOffer } = props;
  const { setToaster } = useContext(Context);

  const user = getUser();

  const handleLikeClick = (action) => {
    axiosService
      .post(`/offer/${offer.id}/${action}/`)
      .then(() => {
        refresh();
      })
      .catch((err) => console.error(err));
  };

  const handleDelete = () => {
    axiosService
      .delete(`/offer/${offer.id}/`)
      .then(() => {
        setToaster({
          type: "warning",
          message: "Offer deleted 🚀",
          show: true,
          title: "Offer Deleted",
        });
        refresh();
      })
      .catch(() => {
        setToaster({
          type: "danger",
          message: "An error occurred.",
          show: true,
          title: "Offer Error",
        });
      });
  };

  return (
    <>
      <Card className="rounded-3 my-4" data-testid="offer-test">
        <Card.Body>
          <Card.Title className="d-flex flex-row justify-content-between">
            <div className="d-flex flex-row">
              <Image
                src={offer.author.avatar}
                roundedCircle
                width={48}
                height={48}
                className="me-2 border border-primary border-2"
              />
              <div className="d-flex flex-column justify-content-start align-self-center mt-2">
                <p className="fs-6 m-0">{offer.author.name}</p>
                <p className="fs-6 fw-lighter">
                  <small>{format(offer.created)}</small>
                </p>
              </div>
            </div>
            {user.name === offer.author.name && (
              <div>
                <Dropdown>
                  <Dropdown.Toggle as={MoreToggleIcon} />
                  <Dropdown.Menu>
                    <UpdateOffer offer={offer} refresh={refresh} />
                    <Dropdown.Item
                      onClick={handleDelete}
                      className="text-danger"
                    >
                      Delete
                    </Dropdown.Item>
                  </Dropdown.Menu>
                </Dropdown>
              </div>
            )}
          </Card.Title>
          <Card.Text>{offer.body}</Card.Text>
          <div className="d-flex flex-row justify-content-between">
            <div className="d-flex flex-row">
              <LikeFilled
                style={{
                  color: "#fff",
                  backgroundColor: "#0D6EFD",
                  borderRadius: "50%",
                  width: "18px",
                  height: "18px",
                  fontSize: "75%",
                  padding: "2px",
                  margin: "3px",
                }}
              />
              <p className="ms-1 fs-6">
                <small>{offer.likes_count} like</small>
              </p>
            </div>
            {!isSingleOffer && (
              <p className="ms-1 fs-6">
                <small>
                  <Link to={`/offer/${offer.id}/`}>
                    {offer.comments_count} comments
                  </Link>
                </small>
              </p>
            )}
          </div>
        </Card.Body>
        <Card.Footer className="d-flex bg-white w-50 justify-content-between border-0">
          <div className="d-flex flex-row">
            <LikeOutlined
              style={{
                width: "24px",
                height: "24px",
                padding: "2px",
                fontSize: "20px",
                color: offer.liked ? "#0D6EFD" : "#C4C4C4",
              }}
              onClick={() => {
                if (offer.liked) {
                  handleLikeClick("remove_like");
                } else {
                  handleLikeClick("like");
                }
              }}
            />
            <p className="ms-1">
              <small>Like</small>
            </p>
          </div>
          {!isSingleOffer && (
            <div className="d-flex flex-row">
              <CommentOutlined
                style={{
                  width: "24px",
                  height: "24px",
                  padding: "2px",
                  fontSize: "20px",
                  color: "#C4C4C4",
                }}
              />
              <p className="ms-1 mb-0">
                <small>Comment</small>
              </p>
            </div>
          )}
        </Card.Footer>
      </Card>
    </>
  );
}

export default Offer;