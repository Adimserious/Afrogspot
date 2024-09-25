## Introduction 
### Afrogspot
Welcome to Afrogspot, your go-to your premier African online grocery shop! designed to celebrate African-inspired products, art, fashion, and culture. Whether you're looking for everyday essentials or specialty items, we are here to make your shopping experience seamless and enjoyable. Our platform is designed to provide you with the best selection of authentic African products, delivered right to your doorstep. Afrogspot, where tradition meets convenience! from across the African diaspora.

Our aim is to provide a seamless shopping experience that bridges the gap between tradition and modern convenience. We are committed to offering a wide range of authentic African products—from groceries to cultural items—sourced from across the African diaspora and delivered directly to your doorstep. By doing so, Afrogspot fosters a deeper connection with African heritage while supporting communities and promoting sustainable practices.

![Am I Responsive Image]()

Link to live website: [CLICK HERE!](https://afrogspot-e3f40930991f.herokuapp.com/)

## Table of contents
  - [Introduction](#Introduction)
  - [Overview](#Overview)
  - [UX-User-Experience](#UX-User-Experience)
   - [Structural plane](#Structural-plane)
  - [Design Aesthetic](#Design-Aesthetic)
    - [Colour Scheme](#Colour-Scheme)
    - [Typography](#Typography)
    - [Visual Elements](#Visual-Elements)

- [Project planning](#Project-planning) 
  - [Agile methodology project Management with Github](#gile-methodology-project-Management-with-Github) 
     - [Repositories](#Repositories)
     - [Issues and story points allocation](#Issues-and-story-points-allocation)
     - [MoSCoW Prioritisation](#MoSCoW-Prioritisation) 
     - [Project Boards](#Project-Boards)
     - [milestones](#milestones)
     - [user stories](#user-stories)
     - [Epics](#Epics)
- [Scope plan](#Scope-plan)
- [Skeleton and surface](#Skeleton-and-surface) 
    - [wireframes](#wireframes)
- [Database Schema](#Database-Schema)
   - [Entity Relationship Diagram](#Entity-Relationship-Diagram)
   - [ERD Table overview](#ERD-Table-overview)
   - [Relationships](#Relationships)
- [Security](#Security)
   - [Data Encryption](#Data-Encryption)
   - [CSRF Tokens](#CSRF-Tokens)
   - [AllAuth](#AllAuth)
- [Features](#Features)
   - [Existing features](#Existing-features)
   - [functionality](#functionality)
   - [CRUD Functionality](#CRUD-Functionality)
- [Featue remaining to implement](#Featue-remaining-to-implement)
- [Technologies Used](#Technologies-Used)
-  [fontend](#fontend)
-  [backend](#backend)
-  [deployment](#deployment)
-  [version control](#version-control)
-  [development tools](#development-tools)
-  [libraries and frameworks](#libraries-and-frameworks)
-  [validation tools](#validation-tools)
-  [Testing](#Testing)
-  [Cloning and Forking](#Cloning-and-Forking)
-  [Credits](#Credits)

## Overview 
Here's an overview of what you can expect:

Categories: The products are grouped into different categories to make browsing easier for customers. Categories also have friendly names for better user experience.

Products: Afrogspot features a range of products with rich descriptions, prices, discount options, stock levels, and ratings. Each product can be linked to a category and a country of origin, allowing customers to filter by region. Products also offer flexibility with custom attributes such as being vegan or gluten-free, and expiration tracking to ensure freshness.

Country: Products can be categorized by their country of origin, adding a layer of cultural and geographical relevance to the items offered.

Product Variants: Some products come with size and price variations, allowing customers to choose the best size based on their needs and budget. Each variant has its own stock and pricing information.

## UX-User-Experience
## Structural plane
1. Clear Navigation and Structure
Header with Navigation: This includes a navigation bar with links to key areas (home, new arrivals, categories, account). This remains visible as users browse, providing easy access to important pages.

Search Functionality: The search bar is central to the navigation. Making it sure prominent and functional, allowing users to find products quickly. Which includes filters for category, price, and availability.

Categories Dropdown: The category dropdown helps users explore different product types, allowing for easy exploration.

2. Seamless Product Discovery
Product List Page: The products displayed under categories or search results include thumbnails, descriptions,pricing, and links to all products in that category. 

Product Filters: There is an easy-to-use filters for product attributes like “vegan,” “gluten-free,” or by country of origin.

Product Variants: Product variants (e.g., different sizes),are displayed on the product detail page with the relevant prices and stock information.

3. Consistent Branding and Visuals
African-Inspired Design: The imagery, patterns, and color schemes reflects African culture. vibrant, warm colors of green, white, and orange, combined with traditional African patterns in the design of the home page hero image and section, users are greeted with a very attractive African shop where people are seen doing some shopping.

Product Images: product images are of high quality and represent the authenticity of the African products sold.

4. Smooth Checkout Process
Cart and Checkout: The cart icon with the total price and item count are always visible. The checkout process is simple, with clear call-to-action buttons.

Delivery Banner: The banner promoting free delivery on orders above a 50 euros encourages users to spend more. This banner updated and visible on all pages.

5. User-Centric Account Management
Account Menu: The account dropdown menu provides options for login, profile view, and product management for superusers. These pages are simple and easy to navigate.

Profile Page: On the profile page, users are greeted with their names, view their order history, address details, and can update their information easily.

6. Back to Top Button
The back-to-top button ensures that users can quickly return to the top of the page after scrolling through long product listings.

7. Mobile-First Design
Given that a large number of users might access the site via mobile, the design is fully responsive. collapsible menus (as shown in the navigation bar) are utilized effectively for different screen sizes. Product images opens in a separate window when clicked and buttons are touch-friendly, with appropriate spacing for easy interaction on mobile devices.

8. Interactive and Engaging Footer
Social Media Integration: The footer includes social media links and a subscription option, which is great for building a community and keeping users informed. icons for Facebook, Instagram, Tiktok, WhatsApp, platforms where many African businesses thrive are present.

Newsletter Signup: A simple call-to-action for subscribing to the newsletter keeps users connected and engaged.

9. Loading Feedback and Toast Messages
The toast notifications system is in place to display feedback messages to users, such as successful actions or errors and it’s easy to understand.
