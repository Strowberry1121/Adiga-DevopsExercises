import http from 'k6/http';
import { sleep, check } from 'k6';

export default function () {
  let res = http.post('http://<API-SERVICE-IP>/node', JSON.stringify({ type: 'Treasure', name: 'Golden Crown' }), {
    headers: { 'Content-Type': 'application/json' },
  });
  check(res, { 'is status 200': (r) => r.status === 200 });
  sleep(1);
}
