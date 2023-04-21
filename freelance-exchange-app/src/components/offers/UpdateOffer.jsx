import React, { useContext, useState } from "react";
import { Button, Modal, Form, Dropdown } from "react-bootstrap";
import axiosService from "../../helpers/axios";
import { Context } from "../Layout";

function UpdateOffer(props) {
  const { offer, refresh } = props;
  const [show, setShow] = useState(false);
  const [validated, setValidated] = useState(false);
  const [form, setForm] = useState({
    author: offer.author.id,
    body: offer.body,
  });

  const { setToaster } = useContext(Context);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const handleSubmit = (event) => {
    event.preventDefault();
    const updateOfferForm = event.currentTarget;

    if (updateOfferForm.checkValidity() === false) {
      event.stopPropagation();
    }

    setValidated(true);

    const data = {
      author: form.author,
      body: form.body,
    };

    axiosService
      .put(`/offer/${offer.id}/`, data)
      .then(() => {
        handleClose();
        setToaster({
          type: "success",
          message: "Offer updated 🚀",
          show: true,
          title: "Success!",
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
      <Dropdown.Item data-testid="show-modal-form" onClick={handleShow}>
        Modify
      </Dropdown.Item>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton className="border-0">
          <Modal.Title>Update Offer</Modal.Title>
        </Modal.Header>
        <Modal.Body className="border-0">
          <Form
            noValidate
            validated={validated}
            onSubmit={handleSubmit}
            data-testid="update-offer-form"
          >
            <Form.Group className="mb-3">
              <Form.Control
                name="body"
                value={form.body}
                data-testid="offer-body-field"
                onChange={(e) => setForm({ ...form, body: e.target.value })}
                as="textarea"
                rows={3}
              />
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button
            data-testid="update-offer-submit"
            variant="primary"
            onClick={handleSubmit}
          >
            Modify
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
}

export default UpdateOffer;