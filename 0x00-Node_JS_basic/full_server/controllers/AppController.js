// controller for returning on / or "homepage" route

class AppController {
  static getHomepage(req, res) {
    return res.end('Hello Holberton School!');
  }
}

module.exports = AppController;
