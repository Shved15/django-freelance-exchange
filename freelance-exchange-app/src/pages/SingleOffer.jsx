import React from "react";

import Layout from "../components/Layout";
import { Row, Col } from "react-bootstrap";
import { useParams } from "react-router-dom";
import useSWR from "swr";
import { fetcher } from "../helpers/axios";
import { Offer } from "../components/offers";
import CreateComment from "../components/comments/CreateComment";
import Comment from "../components/comments/Comment";

function SingleOffer() {
  const { offerId } = useParams();

  const offer = useSWR(`/offer/${offerId}/`, fetcher);

  const comments = useSWR(`/offer/${offerId}/comment/`, fetcher);

  return (
    <Layout hasNavigationBack>
      {offer.data ? (
        <Row className="justify-content-center">
          <Col sm={8}>
            <Offer offer={offer.data} refresh={offer.mutate} isSingleOffer />
            <CreateComment offerId={offer.data.id} refresh={comments.mutate} />
            {comments.data &&
              comments.data.results.map((comment, index) => (
                <Comment
                  key={index}
                  offerId={offer.data.id}
                  comment={comment}
                  refresh={comments.mutate}
                />
              ))}
          </Col>
        </Row>
      ) : (
        <div>Loading...</div>
      )}
    </Layout>
  );
}

export default SingleOffer;