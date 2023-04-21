import React from "react";
import { useParams } from "react-router-dom";
import Layout from "../components/Layout";
import ProfileDetails from "../components/profile/ProfileDetails";
import useSWR from "swr";
import { fetcher } from "../helpers/axios";
import { Offer } from "../components/offers";
import { Row, Col } from "react-bootstrap";

function Profile() {
  const { profileId } = useParams();

  const user = useSWR(`/user/${profileId}/`, fetcher);

  const offers = useSWR(`/offer/?author__public_id=${profileId}`, fetcher, {
    refreshInterval: 20000,
  });

  return (
    <Layout hasNavigationBack>
      <Row className="justify-content-evenly">
        <Col sm={9}>
          <ProfileDetails user={user.data} />
          <div>
            <Row className="my-4">
              {offers.data?.results.map((offer, index) => (
                <Offer key={index} offer={offer} refresh={offers.mutate} />
              ))}
            </Row>
          </div>
        </Col>
      </Row>
    </Layout>
  );
}

export default Profile;