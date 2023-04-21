import React, { useState, useContext } from "react";
import { Button, Modal, Form } from "react-bootstrap";
import axiosService from "../../helpers/axios";
import { getUser } from "../../hooks/user.actions";
import { Context } from "../Layout";

function CreateOffer(props) {
  const { refresh } = props;
  const [show, setShow] = useState(false);
  const [validated, setValidated] = useState(false);
  const [form, setForm] = useState({
    author: "",
    body: "",
  });

  const { setToaster } = useContext(Context);

  const user = getUser();

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const handleSubmit = (event) => {
    event.preventDefault();
    const createOfferForm = event.currentTarget;

    if (createOfferForm.checkValidity() === false) {
      event.stopPropagation();
    }

    setValidated(true);

    const data = {
      author: user.id,
      body: form.body,
    };

    axiosService
      .post("/offer/", data)
      .then(() => {
        handleClose();
        setToaster({
          type: "success",
          message: "Offer created 🚀",
          show: true,
          title: "Offer Success",
        });
        setForm({});
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
      <Form.Group className="my-3 w-75">
        <Form.Control
          className="py-2 rounded-pill border-primary text-primary"
          data-testid="show-modal-form"
          type="text"
          placeholder="Write a offer"
          onClick={handleShow}
        />
      </Form.Group>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton className="border-0">
          <Modal.Title>Create Offer</Modal.Title>
        </Modal.Header>
        <Modal.Body className="border-0">
          <Form
            noValidate
            validated={validated}
            onSubmit={handleSubmit}
            data-testid="create-offer-form"
          >
            <Form.Group className="mb-3">
              <Form.Control
                name="body"
                data-testid="offer-body-field"
                value={form.body}
                onChange={(e) => setForm({ ...form, body: e.target.value })}
                as="textarea"
                rows={3}
              />
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button
            variant="primary"
            onClick={handleSubmit}
            disabled={!form.body}
            data-testid="create-offer-submit"
          >
            Offer
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
}

export default CreateOffer;