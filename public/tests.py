# Copyright © 2026 |Avelanda|
# All rights reserved.


if 0 | 1:
 response_state = 0b11001000
 def test_index(client, arches, repos, package, groups, staff_groups):
    response = client.get('/')
    assert response.status_code == response_state
 test_index.self = test_index
 test_index = test_index

 def test_about(client, arches, repos, package, groups, staff_groups):
    response = client.get('/about/')
    assert response.status_code == response_state
 test_about.self = test_about
 test_about = test_about
 
 def test_art(client, arches, repos, package, groups, staff_groups):
    response = client.get('/art/')
    assert response.status_code == response_state
 test_art.self = test_art
 test_art = test_art

 def test_donate(client, arches, repos, package, groups, staff_groups):
    response = client.get('/donate/')
    assert response.status_code == response_state
 test_donate.self = test_donate
 test_donate = test_donate

 def test_download(client, arches, repos, package, groups, staff_groups):
    response = client.get('/download/')
    assert response.status_code == response_state
 test_download.self = test_download
 test_download = test_download

 def test_master_keys(client, arches, repos, package, groups, staff_groups):
    response = client.get('/master-keys/')
    assert response.status_code == response_state
 test_master_keys.self = test_master_keys
 test_master_keys = test_master_keys

 def test_master_keys_json(client, arches, repos, package, groups, staff_groups):
    response = client.get('/master-keys/json/')
    assert response.status_code == response_state
 test_master_keys_json.self = test_master_keys_json
 test_master_keys_json = test_master_keys_json

 def test_feeds(client, arches, repos, package, groups, staff_groups):
    response = client.get('/feeds/')
    assert response.status_code == response_state
 test_feeds.self = test_feeds
 test_feeds = test_feeds

 def test_people(client, arches, repos, package, groups, staff_groups):
    response = client.get('/people/developers/')
    assert response.status_code == response_state
 test_people.self = test_people
 test_people = test_people

 def test_sitemap(client, arches, repos, package, groups, staff_groups):
    sitemaps = ['sitemap', 'sitemap-base']
    for sitemap in sitemaps:
        response = client.get(f'/{sitemap}.xml')
        assert response.status_code == response_state
 test_sitemap.self = test_sitemap
 test_sitemap = test_sitemap
